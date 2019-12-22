    1. Could not connect development server error
        a. firstly, after making sure that you are in your project file, this solution helps me:
            i. react-native start
        b. most likely you will get an error with code ENOSPC in this case, use this code:
            i. echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
        c. after that, you run 
            i. react-native start 
        d. again, and you should most likely have your ENOSPC error solved. next, just run
            i.  react-native run-android
        e. there you go, it works for me in linux with android emulator from android studio
    2. Command failed: ./gradlew installDebug (Build Failed)
        a. Check USB Debugging is “ON”
        b. Set ANDROID HOME VARIABLE properly
        c. Set permission of android/gradlew to “755”

