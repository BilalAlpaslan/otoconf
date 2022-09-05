from pathlib import Path
from typing import Optional

import typer

from resolvers import nginx_resolver

app = typer.Typer()


@app.command()
def main(type: Optional[str] = typer.Option('nginx', "--type", "-t"),  conf: Optional[Path] = Path('nginx.conf'), output: Optional[Path] = Path('build/nginx.conf')):
    if not conf.exists():
        typer.echo(f"{conf} does not exist", err=True)
        raise typer.Exit(code=1)

    if type == 'nginx':
        nginx_resolver(conf, output)
    else:
        typer.echo("Only nginx is supported for now")


if __name__ == "__main__":
    app()
