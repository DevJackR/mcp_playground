# dbt_tools.py

import subprocess
from mcp import tool

def run_dbt_command(command: list[str]) -> str:
    try:
        result = subprocess.run(
            ["dbt"] + command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=False,
        )
        return result.stdout
    except Exception as e:
        return f"❌ Error running DBT command: {str(e)}"


@tool
async def dbt_run(select: str = "") -> str:
    """Run dbt models. Optionally pass `select` to target specific models."""
    args = ["run"]
    if select:
        args += ["--select", select]
    return run_dbt_command(args)


@tool
async def dbt_test(select: str = "") -> str:
    """Run dbt tests. Optionally pass `select` to target specific models."""
    args = ["test"]
    if select:
        args += ["--select", select]
    return run_dbt_command(args)


@tool
async def dbt_build(select: str = "") -> str:
    """Build dbt models. Combines run, test, and snapshot."""
    args = ["build"]
    if select:
        args += ["--select", select]
    return run_dbt_command(args)


@tool
async def dbt_debug() -> str:
    """Run dbt debug to verify connection and configuration."""
    return run_dbt_command(["debug"])


@tool
async def dbt_docs_generate() -> str:
    """Generate dbt documentation artifacts."""
    return run_dbt_command(["docs", "generate"])


@tool
async def dbt_docs_serve() -> str:
    """Serve dbt docs locally."""
    return run_dbt_command(["docs", "serve"])


@tool
async def dbt_ls(select: str = "") -> str:
    """List nodes in the dbt project."""
    args = ["ls"]
    if select:
        args += ["--select", select]
    return run_dbt_command(args)


@tool
async def dbt_clean() -> str:
    """Clean all dbt artifacts and build directories."""
    return run_dbt_command(["clean"])
