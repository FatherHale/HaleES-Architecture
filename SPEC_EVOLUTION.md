# Spec Evolution

This document explains how the public HaleES architecture specification is expected to grow.

The production HaleES runtime remains closed.

The public specification can still evolve in useful ways without exposing the private engine.

## Current Focus

The current public focus is simple.

1. Make the contract format easier to understand.
2. Make the grading rubric easier to test.
3. Add public safe examples from real operational patterns.
4. Add reference validators that check public shape, not private logic.
5. Keep the boundary clear between open specification and closed runtime.

## What Will Improve Over Time

The contract specification can improve through clearer examples, better field definitions, safer language around authority, and stronger distinction between recommendation and execution.

The grading rubric can improve through more calibration examples, clearer pass and fail cases, better feedback examples, and more guidance on when human review should happen.

The example library can improve through more operational scenarios that show different risk levels, privacy needs, and inference placement choices.

The reference validators can improve by checking whether a public contract includes the required sections and whether a public grading result includes the required score fields.

## What Will Not Be Opened Here

This public repository will not open the production Sensei OS runtime.

It will not open private model routing.

It will not open private memory implementation.

It will not open customer data, private datasets, deployment systems, commercial product code, or internal execution engines.

The public spec explains the pattern.

The private product remains the machine.

## Near Term Public Roadmap

1. Add more public examples for hospitality operations.
2. Add more pass and fail grading samples.
3. Add simple contract validation examples in plain Python.
4. Add a public checklist for reviewing contract quality.
5. Add a public glossary for core terms like authority, contract, grading, inference, privacy boundary, and audit.

## Contribution Direction

Useful public contributions should improve clarity, examples, validator shape, documentation, or rubric calibration.

They should not include secrets, private data, private runtime details, or speculative claims.

The standard is simple.

Make the public pattern easier to understand without exposing what should stay protected.
