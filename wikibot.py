
import wikipedia
import click


@click.command()
@click.option('--name')
def scrape(name="Microsoft"):
    result = wikipedia.summary(name, sentences=1)
    click.echo(click.style(result))


def scrape_withoutCli(name):
    result = wikipedia.summary(name, sentences=1)
    return result

if __name__ == "__main__":
    scrape()
