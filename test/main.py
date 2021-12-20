#coding=utf-8

import os
import requests
from bs4 import BeautifulSoup
import json
import threading

class VideoFetcher:
    def __init__(self):
        pass

    def init(self):
        self.todoList=[]
        self.currentJson={}
    
    def _getTodo(self):
        # Get current status
        modelData=''
        with open('out.txt','r',encoding='utf-8',errors='ignore') as f:
            modelData=f.read()
        modelData=modelData.split()
        for item in modelData:
            if not os.path.exists(f'data/{item}/info.json'):
                self.todoList.append(item)
        if not item:
            print('Finished')
            exit(0)

    def _loadJson(self,pageNumber):
        with open(f'data/{pageNumber}/{pageNumber}.json') as f:
            self.currentJson=json.load(f)
    
    def _getAllVideoLink(self):
        # From currentJson get data
        playlist=self.currentJson['Playlist']
        for index,episode in enumerate(playlist):
            episode[0]=self._getAllVideoLink(episode[0])
            playlist[index]=episode
        


    def _getVideoLink(self,videoID):

        