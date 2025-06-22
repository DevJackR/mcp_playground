import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Point directly to your custom MCP DBT server
server_params = StdioServerParameters(
    command="python",
    args=["server.py"],  # <-- Match this to your file structure
)

async def run():
    print("🚀 Starting DBT MCP Client...")
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("\n🔧 Connected to Custom DBT MCP Server.")

            tools = await session.list_tools()
            print("\n📦 Available DBT Tools:\n")

            for tool in tools.tools:
                print(f"• 🛠️  {tool.name}")
                print(f"  📘 Description: {tool.description or 'No description provided.'}\n")

if __name__ == "__main__":
    asyncio.run(run())