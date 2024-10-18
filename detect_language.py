from lingua import Language, LanguageDetectorBuilder

# Step 1: Initialize the detector with desired languages
detector = LanguageDetectorBuilder.from_languages(
    Language.ENGLISH, Language.FRENCH, Language.SPANISH, Language.GERMAN
).build()

# Step 2: Input some text
text = input("Enter text to detect language: ")

# Step 3: Detect the language
detected_language = detector.detect_language_of(text)

# Step 4: Output the result
if detected_language:
    print(f"The detected language is: {detected_language.name}")
else:
    print("Could not detect the language.")
 