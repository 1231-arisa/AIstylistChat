---
title: AIstylist
emoji: 👗
colorFrom: pink
colorTo: purple
sdk: docker
pinned: false
license: mit
short_description: AI-powered personal fashion stylist
---

# AIstylist

AIstylist is an AI-powered personal fashion assistant that provides outfit suggestions based on your questions. Ask questions like "What should I wear for a rainy Monday at work?" and get detailed styling recommendations.

## Features

- 🤖 **AI-Powered Suggestions**: Uses Together AI with DeepSeek model for intelligent fashion advice
- 🎨 **Structured Recommendations**: Provides color palettes, materials, garment types, and complete outfit coordination
- 🌤️ **Weather-Aware**: Considers weather conditions and temperature for appropriate suggestions
- 💬 **Interactive Interface**: Simple, user-friendly web interface for asking fashion questions
- ⚡ **Fast Responses**: Quick AI-generated styling suggestions

## How to Use

1. Enter your fashion question in the text area
2. Click "Get outfit suggestions"
3. Receive detailed styling recommendations including:
   - Color palette suggestions
   - Material recommendations
   - Specific garment types
   - Complete outfit coordination

## Example Questions

- "What should I wear for a job interview?"
- "I need an outfit for a summer wedding"
- "What's appropriate for a casual Friday at work?"
- "Help me style for a first date"

## Technical Details

- **Framework**: Flask (Python)
- **AI Model**: DeepSeek-R1-Distill-Llama-70B-free via Together AI
- **Frontend**: HTML/CSS with responsive design
- **Deployment**: Hugging Face Spaces

## API Configuration

This app requires a Together API key. Set it as an environment variable:
- `TOGETHER_API_KEY`: Your Together AI API key

## License

MIT License - feel free to use this project for your own fashion applications!