import { Injectable } from '@angular/core';
import { of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MessagesService {

  channels: any[];
  messages: any[];

  constructor() {
    this.channels = ['1', '2', '3'];

    this.messages = [];

    for (let i = 1; i < 11; i++) {
      this.messages.push({
        content: 'Message ' + i,
        date: new Date(),
        writer: 'greg@d82.io',
        channel: '1'
      });
    }
  }


  getChannelsFromAPI() {
    return of(this.channels);
  }


  getMessagesFromAPI() {
    return of(this.messages);
  }

  sendMessage(message: any) {
    this.messages.push(message);
  }
}
