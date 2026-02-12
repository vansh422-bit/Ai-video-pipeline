# Ai-video-pipeline
# 🎬 AI-Powered Automated Video Generation Pipeline

## 📌 Project Overview

This project presents a fully automated AI-driven video generation pipeline that converts a simple user-provided topic into a complete, YouTube-ready MP4 video.

The system integrates multiple AI services and automation tools to generate:
- 📜 AI-written script
- 🎙 AI-generated voiceover
- 🖼 Royalty-free visuals
- 📝 Subtitles
- 🎥 Final rendered video

This project presents a fully automated AI-driven video generation pipeline that transforms a simple user-provided topic into a complete, YouTube-ready MP4 video through intelligent orchestration of multiple AI services and multimedia processing tools. The system is designed to demonstrate real-world AI automation by integrating Large Language Models (Groq / Gemini) for dynamic script generation, Edge TTS for natural-sounding AI voice narration, Pexels API for automatically fetching royalty-free visuals, subtitle generation modules for caption creation, and MoviePy with FFmpeg for seamless video rendering and final composition. The architecture follows a modular and scalable design pattern where each component is independently structured (script generation, voice synthesis, visual retrieval, subtitle processing, and video assembly) but centrally orchestrated through the main execution pipeline. This separation of concerns ensures maintainability, extensibility, and future scalability. The complete automation workflow is illustrated below:
┌──────────────────────────┐
│   User Inputs Topic      │
└─────────────┬────────────┘
              ↓
┌──────────────────────────┐
│ Script Generator (LLM)   │
│ Groq / Gemini API        │
└─────────────┬────────────┘
              ↓
┌──────────────────────────┐
│ Voice Generator (TTS)    │
│ Edge Text-to-Speech      │
└─────────────┬────────────┘
              ↓
┌──────────────────────────┐
│ Visual Fetcher           │
│ Pexels API Integration   │
└─────────────┬────────────┘
              ↓
┌──────────────────────────┐
│ Subtitle Generator       │
│ Caption File Creation    │
└─────────────┬────────────┘
              ↓
┌──────────────────────────┐
│ Video Builder            │
│ MoviePy + FFmpeg         │
└─────────────┬────────────┘
              ↓
┌──────────────────────────┐
│ Final Output: MP4 Video  │
└──────────────────────────┘


