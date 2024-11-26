import { NgModule } from '@angular/core';
import { Routes,RouterModule } from '@angular/router';
import { LoginScreenComponent } from './login-screen/login-screen.component';

export const routes: Routes = [
  { path: '', redirectTo: '/se-connecter', pathMatch: 'full' },
  { path: 'se-connecter', component: LoginScreenComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
