import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {
  loginForm: FormGroup;
  email=''
  password=''
  constructor(private fb:FormBuilder) { 
    this.loginForm=fb.group({
      'email':[this.email,Validators.required],
      'password':[this.email,Validators.required]
    })
  }

  ngOnInit(): void {
  }

  login(post:any){

  }

  signUp(){
    
  }

}
