import { Quality } from "./headerLinks"
import { FaCheck } from "react-icons/fa";
import Images from "../Images/images"


export const HomePage = () => {

    return (
        <div className="flex flex-col lg:flex-row lg:w-[100%]  px-10 lg:px-[50px]">
            <div className="lg:w-[50%] lg:px-[100px]">
                <h1 >
                Lorem ipsum dolor si&nbsp;

                    amet consectetur kier dd.
                </h1>

                <p className="pt-[50px] text-sm lg:text-xl">
                Lorem ipsum dolor sit amet consectetur. Eu aliquam sit sapien scelerisque. Donec iaculis magna elit dictumst aliquam eu odio. 
                Egestas etiam magna nibh elementum in potenti egestas. Sit lobortis fames aliquet nunc eget ut.
                </p>

                <div>

                    <ul class=" text-sm flex py-[50px] flex-col gap-4" aria-labelledby="dropdownDefaultButton">
                        {Quality.map((link) => {
                            return <div className="flex gap-4 items-center">
                                 <div className="lg:w-[40px] w-[20px]
                            lg:h-[40px] h-[20px] rounded-full bg-blue-500 
                            text-2xl p-2 flex justify-center items-center ">
                                <FaCheck className="text-white  "/>
                                </div> 
                                <li className="text-sm lg:text-xl text-bold text-black" key={link.id}>{link.title}</li></div>
                        })}
                    </ul>

                </div>


                <button  className="font-mediu">Get&nbsp;Started</button>
            </div>
            <div className="w-[50%] gap-8 lg:flex justify-center flex-1 hidden ">
                <div className="h-[80%] flex  items-start rounded-3xl w-[30%] bg-red-500">
                    
                <img alt='' className="rounded-3xl w-full h-full" src={Images && Images.home_one} />

                </div>  
                <div className="h-[80%] mt-20 flex items-end rounded-3xl w-[30%] bg-red-500">
                <img alt='' className=" rounded-3xl w-full h-full" src={Images && Images.home_two} />

                </div>

            </div>
        </div>
    )
}