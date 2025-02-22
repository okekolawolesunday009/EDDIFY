import React from 'react'
import { Header } from './header';
import { Title } from '../config/titleHeader';
import { HomePage } from './homePage';
import { Footer } from './footer';
import { Subscribe } from './newsletter';

export default function Layout() {
  Title("Eddify || Home");
  return (
    <div className=''>
        <Header className="-mx-5"  />
        <HomePage/>
        <Subscribe/>
        <Footer/>
        
        {/* homepage
        courses
        whypage
        abtpage
        subscribe
        footer */}


      
    </div>
  )
}
