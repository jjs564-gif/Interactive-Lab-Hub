# Lab 5 Part D: On-Device Qwen Tests

## Test 1: Qwen3.5 0.8B, text reasoning

**Prompt:** Tell me about the history of Roosevelt Island in three sentences.

**Execution time:** 16.4 seconds

**Result:** The model generated a three-sentence response but incorrectly described Roosevelt Island as a World War II military base and associated it with unrelated landmarks.

## Test 2: Qwen3 0.6B, text reasoning

**Prompt:** Tell me about the history of Roosevelt Island in three sentences.

**Execution time:** 5.8 seconds

**Result:** The smaller model responded substantially faster, but its historical claims were also unreliable.

## Test 3: Qwen3.5 0.8B, image reasoning

**Prompt:** What is in this photo?

**Input:** snap.jpg, captured with a USB webcam.

**Execution time:** 33.8 seconds

**Result:** The model described a person with dark hair and short facial hair in front of horizontal blinds. This broadly matched the webcam image.

## Reflection

Both models ran locally on the Raspberry Pi without a cloud inference service. The smaller text model responded faster, while the vision-capable model could interpret an image but required substantially more time.

The experiments demonstrated that a model can generate plausible yet incorrect explanations. For an observant system, the detector's measurements and the interpreter's structured observations should remain separate from the language model's conclusions. The device should not report uncertain or invented events as facts.
