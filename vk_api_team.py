import requests
import vk_api

with open ('VK_token.txt', 'r') as file:
    vk_token = file.readline()

vk_session = vk_api.VkApi(token=vk_token)
vk = vk_session.get_api()
response = vk.account.getProfileInfo()

print(response)