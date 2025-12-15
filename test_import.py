#!/usr/bin/env python3
"""
Test script to check if ohm_mcp.server can be imported
"""
import asyncio
import traceback

import_success = False  # pylint: disable=invalid-name
import_error = None  # pylint: disable=invalid-name

try:
    import ohm_mcp.server
    import_success = True
except ImportError as e:
    import_error = e
    import_success = False


async def test_server():
    """Test the ohm_mcp.server import and basic functionality."""
    try:
        print("Testing import of ohm_mcp.server...")
        if not import_success:
            error_msg = str(import_error) if import_error else "Unknown import error"
            raise ImportError(error_msg)
        print("✓ Import successful")

        print("Testing server instantiation...")
        # Try to access the mcp object
        server = ohm_mcp.server.mcp
        print(f"✓ Server object created: {server}")

        print("Testing tool registration...")
        tools = await server.list_tools()
        print(f"✓ Tools registered: {len(tools)} tools")

        print("All tests passed!")

    except ImportError as e:
        print(f"✗ Import error: {e}")
    except (OSError, ValueError, RuntimeError) as e:
        print(f"✗ Other error: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_server())
