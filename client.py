import re
from SshToServer import SshToServer


def getPrompt(text: str):
    return "Please enter " + text + ": "

def getFileName():
    while True:
        file_name = input(getPrompt("your file name"))
        if file_name and re.match("^[A-Za-z0-9._-]+$", file_name):
            return file_name
        print("Please enter a valid name with characters (not empty).")
        
def getWaitTime(prompt_text):
    while True:
        wait_num = input(getPrompt(prompt_text))
        if wait_num.isdigit():
            return int(wait_num)
        else:
            print(getPrompt("a valid integer for " + prompt_text))
    
def main():
    my_ssh = SshToServer("/Users/davidmarks/Desktop/linux_course/my-first-key-pair.pem", "18.207.203.105", "ubuntu")
    file_name = getFileName()
    wait_time = getWaitTime("how many secconds to wait")
    file_to_run_remote = "final_project.sh"
    remote_cmd = f'./{file_to_run_remote } {file_name} {wait_time}'
    stdout, stderr = my_ssh.runRemoteCommand(remote_cmd)
    if stdout != 0:
        print("Output:", stdout) 
    else:
        print(f"Error: {stderr}")
        

if __name__ == "__main__":
    main()
