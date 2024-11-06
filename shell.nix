let 
    unstable = import (fetchTarball https://nixos.org/channels/nixos-unstable/nixexprs.tar.xz) { };
in
{ pkgs ? import <nixpkgs> {} }:
(pkgs.mkShell {
  name = "pip-env";
  nativeBuildInputs = with pkgs; [
    python311
    virtualenv
    python3Packages.pip
    stdenv.cc
    zlib
  ];

  shellHook = ''
    export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
        pkgs.stdenv.cc.cc
        pkgs.zlib
    ]};
  '';
})
