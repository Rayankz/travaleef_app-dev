import { NgModule } from '@angular/core';
import { Routes,RouterModule } from '@angular/router';
import { LoginScreenComponent } from './login-screen/login-screen.component';
import { VosImpactsComponent } from './vos-impacts/vos-impacts.component';
import { HistoriqueComponent } from './historique/historique.component';
import { AccueilComponent } from './accueil/accueil.component';


export const routes: Routes = [
  //{ path: '', redirectTo: '/se-connecter', pathMatch: 'full' },
  { path: 'se-connecter', component: LoginScreenComponent },
  { path: 'vos-impacts', component: VosImpactsComponent },
  { path: 'historique', component: HistoriqueComponent },
  { path: '', component: AccueilComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
