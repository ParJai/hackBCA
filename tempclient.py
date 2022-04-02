import pygame
import threading

class TempClient:

    def __init__(self, window, clock, client):
        self.window = window
        self.clock = clock

        self.client = client

        self.run = True

        msg = ""
        sending = threading.Thread(target = self.client.send_message, args = (msg,), daemon = True)
        sending.start()
        recieving = threading.Thread(target = self.client.recieve_message, args = (), daemon = True)
        recieving.start()

        while self.run:
            if len(self.client.recievingQueue) != 0:
                print((self.client.recievingQueue[0][0], self.client.recievingQueue[0][1]))
                del self.client.recievingQueue[0]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run == False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.client.messageQueue.append('parth your shitting my balls')
            self.window.fill((255,255,255))
            pygame.display.update()