print("Beginning")
from whisper_mic import WhisperMic
print("Whisper_Mic import")
from cat_helper import move_cat
print("Cat_helper import")

if __name__ == "__main__":
    print("Before the loop")

    while True:
        try:
            mic = WhisperMic()
            print("After initializing WhisperMic")
            command = mic.listen()
            print("Command:", command)
            move_cat(command)
            if command == "fuck off":
                break
        except Exception as e:
            print("An error occurred:", e)
