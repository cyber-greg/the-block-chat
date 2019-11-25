import { Component, OnInit, ViewChild } from '@angular/core';
import { MessagesService } from '../services/messages.service';

@Component({
  selector: 'app-list',
  templateUrl: 'list.page.html',
  styleUrls: ['list.page.scss']
})
export class ListPage implements OnInit {
  @ViewChild('content', { static: false }) content: any;

  private newChat: string;

  messages: any[] = [];
  // messages: Array<{ id?: string, content: string; date: Date; author: string; channel: string }> = [];

  private selectedItem: any;
  private icons = [
    'flask',
    'wifi',
    'beer',
    'football',
    'basketball',
    'paper-plane',
    'american-football',
    'boat',
    'bluetooth',
    'build'
  ];

  public items: any[] = [];

  constructor(
    private messagesService: MessagesService
  ) {
    // for (let i = 1; i < 11; i++) {
    //   this.items.push({
    //     title: 'Item ' + i,
    //     note: 'This is item #' + i,
    //     icon: this.icons[Math.floor(Math.random() * this.icons.length)]
    //   });
    // }

    this.updateMessages('1');
  }

  ngOnInit() {
  }
  // add back when alpha.4 is out
  // navigate(item) {
  //   this.router.navigate(['/list', JSON.stringify(item)]);
  // }

  ionViewDidEnter() {
    this.scrollToBottom();
  }

  updateMessages(channel: string) {
    this.messagesService.getMessagesFromAPI().subscribe((response: any) => {
      console.warn('MESSAGE MOCKUP FROM API', response);
      this.messages = response;
    });
  }

  isMyChat(bubbleContent: any) {
    if (bubbleContent % 2) {
      return true;
    } else {
      return false;
    }
  }

  sendChat() {

    if (!this.newChat) { // if empty do nothing
      return undefined;
    }

    this.messagesService.sendMessage({
      content: this.newChat,
      date: new Date(),
      author: 'greg@d82.io',
      channel: '1'
    }).then((response: any[]) => {
      this.messages = response;
      // this.scrollToBottom();
      setTimeout(() => this.scrollToBottom(), 250); // wait for the list to be locally updated befor scrolling
      this.newChat = undefined;
    });

  }

  scrollToBottom() {
    this.content.scrollToBottom(300);  // 300ms animation speed
  }
}
