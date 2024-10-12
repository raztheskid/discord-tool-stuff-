import os
import requests
import numpy as np
import time
import string

class DiscordTool:
    def __init__(self):
        self.base_url = "https://discord.com/api/v10"
        self.token = None

    def main_menu(self):
        self.token = input("Enter your Discord user token: ")
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠿⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣾⣿⣶⣶⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠘⢿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠈⠻⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⣀⣤⣶⣶⣌⠻⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⠁⣰⣿⣿⣿⣿⣿⣦⡙⢿⣿⣿⣿⠄⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣦⣙⣛⣋⣼⣿⣿⣶⣿⣿⣿⣿⣿⣿⣯⡉⠉⠉⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⡆⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⢻⣿⣿⣿⣿⣿⡇⠀⠀⠈⠉⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣴⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⡇⠀⠸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⢿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣶⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣧⣄⣀⣀⣀⣀⣀⣀⡀
⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    """)
            print("                               ┌───────────────────────────┬───────────────────────────┐")
            print("                               │ DOMAIN.EZ gg/wtV7YrRccB       │                           │")
            print("                               ├───────────────────────────┼───────────────────────────┤")
            print("                               │ [1] Nitro Gen             │ [11] Coming Soon          │")
            print("                               │ [2] Credits               │ [12] Coming Soon          │")
            print("                               │ [3] Calculator            │ [13] Coming Soon          │")
            print("                               │ [4] Create Channels       │ [14] Coming Soon          │")
            print("                               │ [5] Delete Channels       │ [15] Coming Soon          │")
            print("                               │ [6] Webhook Spammer       │ [16] Coming Soon          │")
            print("                               │ [7] Webhook Deleter      │ [17] Coming Soon          │")
            print("                               │ [8] DM (useless)               │ [18] Coming Soon          │")
            print("                               │ [9] Delete DMS            │ [19] Coming Soon          │")
            print("                               │ [10] GC Spam              │ [20] Coming Soon          │")
            print("                               ├───────────────────────────┴───────────────────────────┘")
           






            choice = input("Select an option: ")

            if choice == '1':
                self.nitro_gen()
            elif choice == '2':
                self.show_credits()
            elif choice == '3':
                self.calculator()
            elif choice == '4':
                self.create_channels()
            elif choice == '5':
                self.delete_channels()
            elif choice == '6':
                self.webhook_spammer()
            elif choice == '7':
                self.webhook_deleter()
            elif choice == '8':
                self.dm_bot()
            elif choice == '9':
                self.delete_dms()
            elif choice == '10':
                self.gc_spam()
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")

    def nitro_gen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Nitro Generator")
        num = int(input("how much codes to check (rare to get a working one): "))

        valid_codes = []
        chars = string.ascii_letters + string.digits
        codes = np.random.choice(list(chars), size=(num, 16))

        start_time = time.time()
        for index, s in enumerate(codes):
            code = ''.join(s)
            url = f"https://discord.gift/{code}"
            result = self.quick_checker(url)
            if result:
                valid_codes.append(url)

            self.update_progress(index + 1, num, start_time)

        print(f"\nResults:\n Valid: {len(valid_codes)}\n Valid Codes: {', '.join(valid_codes)}")
        input("enter to go to menu...")

    def quick_checker(self, nitro):
        response = requests.get(f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true",
                                headers={"Authorization": self.token})
        if response.status_code == 200:
            print(f"Valid | {nitro}")
            return True
        else:
            print(f"Invalid | {nitro}")
            return False

    def update_progress(self, current, total, start_time):
        elapsed = time.time() - start_time
        percent = (current / total) * 100
        bar_length = 30
        filled_length = int(bar_length * current // total)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)

        print(f"\r[{bar}] {percent:.2f}% | Elapsed: {elapsed:.2f}s", end='')

    def show_credits(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Credits")
        print("made by dasthefith/raz")
        input("enter to go back to main menu")

    def calculator(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("calculator (no idea why i made this)")
        expression = input("supports multiplication (*), division (/), addition and subtraction (+) (-) ")
        try:
            result = eval(expression)
            print(f"answer: {result}")
        except Exception as e:
            print("Error: invalid expression.")
        input("enter to go back to menu")

    def webhook_spammer(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        webhook_url = input("enter the webhook url: ")
        message = input("enter the message to send: ")
        count = int(input("enter the number of times to send the message: "))

        for _ in range(count):
            response = requests.post(webhook_url, json={"content": message})
            if response.status_code == 204:
                print("Sent")
            else:
                print(f"failed to send message: {response.status_code} | {response.text}")

        input("enter to return to the menu...")

    def webhook_deleter(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        webhook_url = input("enter webhook URL to delete: ")
        response = requests.delete(webhook_url)

        if response.status_code == 204:
            print("Webhook deleted successfully! yippy")
        else:
            print(f"failed to delete webhook: {response.status_code} | {response.text}")

        input("Enter to return to the menu...")

    def create_channels(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        guild_id = input("Enter the server ID: ")
        channel_name = input("Enter the channel name: ")
        num_channels = int(input("Enter the number of channels to create: "))

        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }

        for _ in range(num_channels):
            channel_data = {
                "name": channel_name,
                "type": 0
            }
            response = requests.post(f"{self.base_url}/guilds/{guild_id}/channels", headers=headers, json=channel_data)

            if response.status_code == 201:
                print(f"Channel '{channel_name}' created successfully.")
            elif response.status_code == 401:
                print("invalid token or dont have perms")
                break
            else:
                print(f"failed to create channel: {response.status_code} | {response.text}")

    def delete_channels(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        guild_id = input("Enter your server ID: ")

        headers = {"Authorization": self.token}
        response = requests.get(f"{self.base_url}/guilds/{guild_id}/channels", headers=headers)

        if response.status_code != 200:
            print(f"failed to retrieve channels: {response.status_code} | {response.text}")
            return

        channels = response.json()
        print("Available channels:")
        for channel in channels:
            print(f"{channel['id']}: {channel['name']}")

        channel_id = input("Enter the channel ID to delete: ")
        response = requests.delete(f"{self.base_url}/channels/{channel_id}", headers=headers)

        if response.status_code == 204:
            print("Channel deleted successfully.")
        else:
            print(f"Failed to delete channel: {response.status_code} | {response.text}")

        input("enter to go back to menu")

    def dm_bot(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        user_id = input("Enter the userid to DM: ")
        message = input("Enter the message to send: ")
        num_messages = int(input("Enter how many messages to send: "))

        for _ in range(num_messages):
            response = requests.post(f"{self.base_url}/channels/{user_id}/messages", headers={"Authorization": self.token}, json={"content": message})

            if response.status_code == 200:
                print("Message sent.")
            else:
                print(f"Failed to send message: {response.status_code} | {response.text}")

        input("Press Enter to return to the main menu...")

    def delete_dms(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        user_id = input("userid of the person you want to delete your dms with: ")

        headers = {"Authorization": self.token}
        dm_channel = requests.post(f"{self.base_url}/users/@me/channels", 
                                   json={"recipient_id": user_id}, headers=headers)
        
        if dm_channel.status_code == 200:
            channel_id = dm_channel.json()["id"]
            messages = requests.get(f"{self.base_url}/channels/{channel_id}/messages?limit=100", headers=headers).json()

            while messages:
                for msg in messages:
                    msg_id = msg["id"]
                    requests.delete(f"{self.base_url}/channels/{channel_id}/messages/{msg_id}", headers=headers)
                    print(f"Deleted message: {msg_id}")
                messages = requests.get(f"{self.base_url}/channels/{channel_id}/messages?limit=100", headers=headers).json()
            
            print("All messages deleted successfully.")
        else:
            print(f"ailed to delete dm: {dm_channel.status_code} | {dm_channel.text}")

        input("enter to go back to menu")

    def gc_spam(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        user_ids = input("Enter two user IDs separated by a comma: ").split(',')
        num_chats = int(input("Enter how many GC(s) to create: "))
        
        leave_gc = input("Do you want to leave the GC(s) after they are created? Y/N: ").lower()
        
        if leave_gc == 'y':
            use_delay = input("Do you want to use a delay (to avoid rate limits and also reccomended)? y/n: ").lower()
            delay = 0
            if use_delay == 'y':
                delay = float(input("Enter the delay in seconds: "))

            for _ in range(num_chats):
                chat_data = {
                    "recipients": [user_ids[0].strip(), user_ids[1].strip()]
                }
                response = requests.post(f"{self.base_url}/users/@me/channels", headers={"Authorization": self.token}, json=chat_data)

                if response.status_code == 200:
                    channel_id = response.json()["id"]
                    print("GC created.")
               
                    requests.delete(f"{self.base_url}/channels/{channel_id}", headers={"Authorization": self.token})
                    print("Left GC.")
                else:
                    print(f"failed to create GC: {response.status_code} | {response.text}")

                if use_delay == 'y':
                    time.sleep(delay)

        else:  
            for _ in range(num_chats):
                chat_data = {
                    "recipients": [user_ids[0].strip(), user_ids[1].strip()]
                }
                response = requests.post(f"{self.base_url}/users/@me/channels", headers={"Authorization": self.token}, json=chat_data)

                if response.status_code == 200:
                    print("GC created.")
                else:
                    print(f"Failed to create GC: {response.status_code} | {response.text}")

        input("enter to go back to menu")


if __name__ == "__main__":
    tool = DiscordTool()
    tool.main_menu()
