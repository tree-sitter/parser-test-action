# Tree-sitter parser tests

## Options

```yaml
generate:
  description: Verify the generated parser
  default: true
abi-version:
  description: The tree-sitter ABI version
  default: "15"

test-parser:
  description: Test the parser
  default: true
test-parser-cmd:
  description: Command that tests the parser
  default: tree-sitter test

test-rust:
  description: Test the Rust bindings
  default: false
rust-version:
  description: Rust version
  default: stable

test-node:
  description: Test the Node bindings
  default: false
node-version:
  description: Node.js version
  default: latest

test-python:
  description: Test the Python bindings
  default: false
python-version:
  description: Python version
  default: "3.11"

test-go:
  description: Test the Go bindings
  default: false
go-version:
  description: Go version
  default: "1.23"

test-swift:
  description: Test the Swift bindings
  default: false
swift-version:
  description: Swift version
  default: "5.10"
```

## Example configuration

```yaml
name: CI

on:
  push:
    branches: [master]
    paths:
      - grammar.js
      - src/**
      - bindings/**
      - binding.gyp
  pull_request:
    paths:
      - grammar.js
      - src/**
      - bindings/**
      - binding.gyp

concurrency:
  group: ${{github.workflow}}-${{github.ref}}
  cancel-in-progress: true

jobs:
  test:
    name: Run tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: tree-sitter/setup-action/cli@v1
      - uses: tree-sitter/parser-test-action@v2
        with:
          abi-version: 14
          test-rust: true
```
