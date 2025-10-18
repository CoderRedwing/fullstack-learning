import { useState } from 'react'
import './App.css'
import Card from './components/Card'

function App() {

  const nftData = [
    {
      id: 345,
      name: "Bored Ape #1",
      price: "0.01 ETH",
      image:
        "https://cdn.vox-cdn.com/thumbor/ZkmdkuJUTLgJh96_FWQ5zweGGxo=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/23084330/bored_ape_nft_accidental_.jpg",
    },
    {
      id: 678,
      name: "Bored Ape #2",
      price: "0.05 ETH",
      image:
        "n.io/gae/x-gUdIb93bfTu8pZULZRmQ9Qjs5y6Hb-mzOnPIfI9q3p4P02jC4KxWnEyX_r9y6qU-RYoIphWzbfvfr2xARqoyVb2j6mvzMezKo0zQ?auto=format&dpr=1&w=100",
    },
    {
      id: 999,
      name: "Bored Ape #3",
      price: "0.10 ETH",
      image:
        "https://www.lifewire.com/thmb/MU-pPL5LK7b7vFLszTZbRO41Vx4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/bored-ape-nft-5c07a5d4df8240bfbcc6c6213951b12e.png",
    },

    {
      id: 999,
      name: "Bored Ape #4",
      price: "0.10 ETH",
      image:
        "https://www.lifewire.com/thmb/MU-pPL5LK7b7vFLszTZbRO41Vx4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/bored-ape-nft-5c07a5d4df8240bfbcc6c6213951b12e.png",
    },

  ];

  return (
    <>
      <h1 className="bg-green-500 text-black rounded-xl mb-4">Day 2 of learning react</h1>
      <div className="flex justify-between">
        {nftData.map((item) => (
        <Card key={item.id} // Always add a unique key
            id={item.id}
            name={item.name}
            price={item.price}
            image={item.image}/>
      ))}
      </div>
    </>
  )
}

export default App
