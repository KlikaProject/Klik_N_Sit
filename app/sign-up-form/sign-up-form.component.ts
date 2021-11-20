import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-sign-up-form',
  templateUrl: './sign-up-form.component.html',
  styleUrls: ['./sign-up-form.component.css']
})
export class SignUpFormComponent implements OnInit {
  loginForm: FormGroup;
  name=''
  email=''
  password=''
  passwordConfirm=''
  constructor(private fb:FormBuilder) { 
    this.loginForm=fb.group({
      'name':[this.name,Validators.required],
      'email':[this.email,Validators.required],
      'password':[this.password,Validators.required],
      'passwordConfirm':[this.passwordConfirm,Validators.required]
    })
  }

  ngOnInit(): void {
  }

  login(post:any){

  }

  signUp(){
    
  }

}
