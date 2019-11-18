import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class MessagesService {

  apiUrl = `${environment.API}`;

  channels: any[];
  messages: any[];

  constructor(
    private http: HttpClient,
  ) {
    this.channels = ['1', '2', '3'];
    this.messages = [];
  }


  getChannelsFromAPI() {
    return of(this.channels);
  }


  getMessagesFromAPI(): Observable<object> {
    return this.http.get(`${this.apiUrl}/chat/`);
  }


  sendMessage(message: any) {
    const messageJSON = JSON.stringify(message);

    return new Promise((resolve, reject) => {
      this.http.post(`${this.apiUrl}/chat/`, messageJSON)
        .subscribe((res: any) => {
          console.warn('API POST MESSAGE res', res);
          resolve(res);
        }, (err) => {
          console.error('API POST MESSAGE res', err);
          reject(err);
        });
    });
  }
}
