import { Component, OnInit} from '@angular/core';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  // @ViewChild('carousel') carousel: ElementRef;

  constructor() { }

  ngOnInit() {
  }
  ngAfterViewInit(){

  }

  scrollTo(id){
    let $scrollTo = $('#'+id);
    $('html,body').animate({scrollTop: $scrollTo.offset().top});

  }



}
