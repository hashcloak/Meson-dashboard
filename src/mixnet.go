package main

import (
	"context"
	"encoding/json"
	"fmt"
	"time"

	"github.com/katzenpost/client"
	"github.com/katzenpost/client/config"
	"github.com/katzenpost/core/epochtime"
	"github.com/katzenpost/core/log"
)

// CFG is the config
var CFG = `
[Logging]
  Disable = false
  Level = "ERROR"
  File = ""
[UpstreamProxy]
  Type = "none"
[Debug]
  DisableDecoyTraffic = true
  CaseSensitiveUserIdentifiers = false
  PollingInterval = 1
[NonvotingAuthority]
		Address = "%s"
    PublicKey = "%s"
`

func main() {
	authPubKey := "qVhmF/rOHVbHwhHBP6oOOP7fE9oPg4IuEoxac+RaCHk="
	authAddress := "159.65.210.250:30000"

	cfg, err := config.Load([]byte(fmt.Sprintf(CFG, authAddress, authPubKey)))

	if err != nil {
		panic("ERROR In creating new client: " + err.Error())
	}

	c, err := client.New(cfg)
	if err != nil {
		panic("ERROR In creating new client: " + err.Error())
	}

	logFilePath := ""
	backendLog, err := log.New(logFilePath, "ERROR", false)
	if err != nil {
		panic(err)
	}
	proxyCfg := cfg.UpstreamProxyConfig()
	pkiClient, err := cfg.NewPKIClient(backendLog, proxyCfg)
	if err != nil {
		panic(err)
	}
	currentEpoch, _, _ := epochtime.FromUnix(time.Now().Unix())
	ctx, cancel := context.WithTimeout(context.Background(), 45*time.Second)
	defer cancel()

	doc, _, err := pkiClient.Get(ctx, currentEpoch)
	if err != nil {
		panic(err)
	}

	documentJSON, err := json.MarshalIndent(doc, "", " ")
	if err != nil {
		panic(err)
	}
	cfgJSON, err := json.MarshalIndent(cfg, "", " ")
	if err != nil {
		panic(err)
	}
	fmt.Printf(`{
		"Document": %s,
		"Config": %s
	}`, documentJSON, cfgJSON)

	c.Shutdown()
}
