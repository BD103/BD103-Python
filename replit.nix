{ pkgs }: {
    deps = [
        pkgs.python38
        pkgs.poetry
        pkgs.vim
        pkgs.nodePackages.prettier
    ];
}
