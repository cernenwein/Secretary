#!/bin/bash
set -x

echo "📥 Simulating voice input..."
docker exec diane-voice bash -c 'echo "Remember that I prefer copper wiring." > /shared_memory/voice_input.txt'

echo "⏳ Waiting 5 seconds for planner and TTS to process..."
sleep 5

echo "📤 Checking planner output:"
docker exec diane-planner cat /shared_memory/planner_output.txt || echo "No planner output found."

echo "🧠 Checking memory.json:"
docker exec diane-planner cat /shared_memory/memory.json | jq '.facts' || echo "No memory found."
