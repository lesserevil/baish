# baish
A version of bash that also knows what you were probably _trying_ to do.

## Repository Structure

```
├── bash-handbook-review/
│   └── REVIEW.md                # Comprehensive review of the bash-handbook
├── bash-source/
│   ├── builtins/
│   │   └── mcp.def             # MCP builtin implementation
│   ├── test-mcp.sh             # MCP test script
│   └── README.md               # Instructions for bash 5.3 source
├── IMPLEMENTATION-SUMMARY.md   # MCP implementation details
├── MCP-IMPLEMENTATION.md       # MCP feature documentation
├── LICENSE
└── README.md                   # This file
```

## Features

### MCP (Managed Control Points) Support ✨ NEW

Baish now includes AI-enabled functionality through MCP (Managed Control Points) integration:

- **`mcp connect <server>`** - Connect to MCP servers for AI-powered capabilities
- **`mcp disconnect`** - Disconnect from active MCP server
- **`mcp list`** - List available commands from connected MCP server

See [MCP-IMPLEMENTATION.md](MCP-IMPLEMENTATION.md) for complete documentation and usage examples.

#### Quick Start

```bash
# Build baish with MCP support
cd bash-source
./configure
make

# Test MCP functionality
./bash test-mcp.sh

# Connect to an MCP server (requires running MCP server)
./bash -c "mcp connect localhost:8080"
./bash -c "mcp list"
./bash -c "mcp disconnect"
```

#### Requirements

- libcurl development library (`libcurl4-openssl-dev` on Ubuntu/Debian)
- Standard build tools (gcc, make, etc.)

## Development Resources

### 1. Bash Handbook Review
Located in `bash-handbook-review/REVIEW.md`, this document provides:
- Overview of bash fundamentals from https://github.com/denysdovhan/bash-handbook
- Key concepts and features
- Common user mistakes to address
- Insights for implementing intelligent error correction
- Relevance to the baish project goals

### 2. Bash Source Code Reference
The `bash-source/` directory contains the bash 5.3 source code with baish enhancements. Having access to the actual bash implementation helps with:
- Understanding bash's internal behavior
- Ensuring compatibility
- Learning from established patterns
- Implementing similar features with enhancements

See `bash-source/README.md` for build instructions.

## Key Features to Implement

Based on the bash handbook review, baish could help with:
- Variable quoting mistakes
- Typos in command names
- Incorrect conditional syntax
- Misused exit codes
- Array handling errors
- Redirection mistakes
- Common scripting anti-patterns

## Building from Source

```bash
# Install dependencies (Ubuntu/Debian)
sudo apt-get install build-essential libcurl4-openssl-dev

# Configure and build
cd bash-source
./configure --prefix=/usr/local
make

# Run tests
./bash test-mcp.sh

# Install (optional)
sudo make install
```

## Contributing

Contributions are welcome! When adding new features:

1. Follow bash's established patterns for built-ins
2. Ensure memory safety (check all allocations)
3. Add comprehensive tests
4. Update documentation
5. Run security checks

See [IMPLEMENTATION-SUMMARY.md](IMPLEMENTATION-SUMMARY.md) for development insights.

## License

Baish is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
