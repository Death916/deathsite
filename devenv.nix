{
  pkgs,
  lib,
  config,
  inputs,
  ...
}:

{
  # https://devenv.sh/basics/
  env.GREET = "deathsite";

  # https://devenv.sh/packages/
  packages = [
    pkgs.git
    pkgs.uv
  ];

  # https://devenv.sh/languages/
  languages.python = {
    enable = true;
    version = "3.14";
    uv = {
      enable = true;
      sync = {
        enable = true;
        allGroups = true;
      };
    };
  };

  # https://devenv.sh/scripts/
  scripts.hello.exec = ''
    echo hello from $GREET
  '';

  # https://devenv.sh/basics/
  enterShell = ''
    hello
    echo "Python : $(python --version)"
    echo "UV     : $(uv --version)"
    # Put uv-managed venv bin on PATH so reflex (and other CLI tools) work directly
    export PATH="${config.devenv.state}/venv/bin:$PATH"
  '';

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    python --version | grep --color=auto "3.11"
    uv --version
    uv run python -c "import googleapiclient; print('google-api-python-client OK')"
    uv run python -c "import reflex; print('reflex OK')"
  '';
}
