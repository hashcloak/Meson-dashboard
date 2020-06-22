let
  sources = import ./nix/sources.nix;
  pkgs = import sources.nixpkgs {};
  libPath = pkgs.stdenv.lib.makeLibraryPath [pkgs.stdenv.cc.cc];
in pkgs.mkShell rec {
  name = "meson-dashboard";
  venvDir = "./.venv";
  buildInputs = [
    pkgs.python38Packages.python
    pkgs.python38Packages.venvShellHook
    pkgs.stdenv.cc.cc
  ];
  LD_LIBRARY_PATH="${libPath}";
  #  https://github.com/NixOS/nixpkgs/blob/master/doc/languages-frameworks/python.section.md#python-setuppy-bdist_wheel-cannot-create-whl
  # https://github.com/NixOS/nixpkgs/issues/270
  SOURCE_DATE_EPOCH=315532800; 
  postShellHook = ''
    pip install -r requirements.txt
  '';
}
