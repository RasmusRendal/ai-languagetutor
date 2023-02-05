{
    description = "A very basic flake";

    inputs = {
        nixpkgs.url = "github:nixos/nixpkgs";
        flake-utils.url = "github:numtide/flake-utils";
    };

    outputs = { self, flake-utils, nixpkgs }:
    flake-utils.lib.eachDefaultSystem (system:
    let
        python = "python310";
        pkgs = import nixpkgs { inherit system; };
        mPython = pkgs.${python}.withPackages (ps: with ps; [ openai ]);
    in
    {
        defaultPackage = pkgs.stdenv.mkDerivation {
            name = "tutor";
            version = "0.10";
            buildInputs = with pkgs; [ mPython languagetool ];
            src = ./.;
        };
    });
}
