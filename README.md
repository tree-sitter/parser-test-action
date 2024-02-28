# Tree-sitter parser tests

## Options

```yaml
lint:
  description: Enable linting
  default: false
generate:
  description: Verify the generated parser
  default: false
test-grammar:
  description: Test the grammar
  default: true
test-library:
  description: Test the rust library
  default: true
corpus-files:
  description: Glob patterns of files to parse
invalid-files:
  description: Glob patterns of files with syntax errors
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

jobs:
  test:
    name: Run tests
    runs-on: ubuntu-latest
    steps:
      - uses: tree-sitter/parser-setup-action@v1.1
        with:
          node-version: 20
      - uses: tree-sitter/parser-test-action@v1.2
        with:
          corpus-files: |-
            examples/*
```
