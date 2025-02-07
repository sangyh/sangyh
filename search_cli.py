#!/usr/bin/env python3

import sys
import argparse
from pathlib import Path
from enhanced_search import EnhancedSearch
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.panel import Panel
from rich import print as rprint

def create_parser():
    parser = argparse.ArgumentParser(description="Search through notes with an enhanced CLI interface")
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument(
        "-m", "--mode",
        choices=["all", "exact", "fuzzy"],
        default="all",
        help="Search mode (default: all)"
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Show preview of matched files"
    )
    return parser

def display_results(results, show_preview=False):
    console = Console()
    
    if not results:
        console.print("\n[yellow]No results found[/yellow]")
        return
    
    # Create results table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("№", style="dim", width=4)
    table.add_column("Title", style="cyan")
    table.add_column("Match", style="green")
    table.add_column("Score", justify="right", width=8)
    table.add_column("Path", style="dim")
    
    for i, result in enumerate(results, 1):
        table.add_row(
            str(i),
            result.title,
            result.match_type,
            f"{result.score:.2f}",
            str(result.file)
        )
    
    console.print("\n")
    console.print(table)
    
    if show_preview:
        console.print("\n[bold]Previews:[/bold]\n")
        for i, result in enumerate(results, 1):
            panel = Panel(
                Markdown(f"```\n{result.snippet}\n```"),
                title=f"[cyan]{i}. {result.title}[/cyan]",
                subtitle=f"[dim]{result.file}[/dim]"
            )
            console.print(panel)
            console.print()

def interactive_mode(searcher):
    """Interactive search mode with real-time results."""
    console = Console()
    
    console.print("[bold green]Interactive Search Mode[/bold green]")
    console.print("Type your search query (or 'quit' to exit)")
    
    while True:
        try:
            query = input("\n> ")
            if query.lower() in ('quit', 'exit', 'q'):
                break
            
            if not query.strip():
                continue
            
            results = searcher.search(query)
            display_results(results, show_preview=True)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"[red]Error:[/red] {str(e)}")
    
    console.print("\n[green]Goodbye![/green]")

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    searcher = EnhancedSearch()
    
    if not args.query:
        interactive_mode(searcher)
        return
    
    results = searcher.search(args.query, args.mode)
    display_results(results, show_preview=args.preview)

if __name__ == "__main__":
    main()
