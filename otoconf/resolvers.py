

import re
from pathlib import Path

import nginxfmt
import typer


def read_conf(config: Path):
    """Reads the configuration file"""
    return Path(config).read_text()


def nginx_resolver(conf: Path, output: Path):
    """Resolves nginx configuration files
    
    @{% 'path/.conf' %} read .conf and replace with content
    """
    file = conf.read_text()
    for index, line in enumerate(file.splitlines()):
        if re.search(r'@{%', line):
            start = line.find('@{%')
            end = line.find('%}')
            path = line[start+3:end].replace(' ', '').replace("'", '').replace('"', '')

            conf = Path(path)
            if conf.exists():
                file = file.replace(line, conf.read_text())
            else:
                typer.echo(f'File {conf} does not exist (line {index + 1})')
                raise typer.Exit(1)


    output_dir = output.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    f = output.open('w')
    fmt = nginxfmt.Formatter()
    f.write(fmt.format_string(file))
    f.close()

    typer.echo(f'Configuration file {output} created')