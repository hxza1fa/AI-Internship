import Image, { type StaticImageData } from "next/image";
import localFont from "next/font/local";
import priceDistribution from "../images/diamond-price-distribution.png";
import caratVsPrice from "../images/carat-vs-price.png";
import meanPriceByCut from "../images/mean_price_by_cut.png";
import meanPriceByColor from "../images/mean_price_by_color.png";
import meanPriceByClarity from "../images/mean_price_by_clarity.png";
import heatmap from "../images/heatmap.png";

const dmSansRegular = localFont({
  src: "../fonts/dm-sans/DMSans_18pt-Regular.ttf",
  display: "swap",
});

const dmSansBold = localFont({
  src: "../fonts/dm-sans/DMSans_36pt-Bold.ttf",
  display: "swap",
});

const cards: { title: string; image?: StaticImageData }[] = [
  { title: "Price Distribution", image: priceDistribution },
  { title: "Carat vs Price", image: caratVsPrice },
  { title: "Average Price by Cut", image: meanPriceByCut },
  { title: "Average Price by Color", image: meanPriceByColor },
  { title: "Average Price by Clarity", image: meanPriceByClarity },
  { title: "Feature Correlation", image: heatmap },
];

export default function Home() {
  return (
    <section className="p-8">
      <div className="mb-8 text-center">
        <h1
          className={`${dmSansBold.className} text-[#f5f5f5] text-[36px] tracking-tight`}
        >
          Diamond Insights 2022
        </h1>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        {cards.map(({ title, image }) => (
          <article
            key={title}
            className="flex min-h-[28rem] flex-col rounded-lg bg-white shadow-lg transition-all duration-200 hover:-translate-y-1 hover:shadow-xl"
          >
            <h2
              className={`${dmSansRegular.className} px-6 pt-6 pb-3 text-center text-[20px] text-black`}
            >
              {title}
            </h2>
            <div className="relative mx-6 mb-6 flex-1 min-h-80">
              {image ? (
                <Image
                  src={image}
                  alt={title}
                  fill
                  className="object-contain"
                  sizes="(max-width: 768px) 100vw, 33vw"
                />
              ) : null}
            </div>
          </article>
        ))}
      </div>
      <div className="mb-8 pt-8 text-center">
        <h1
          className={`${dmSansBold.className} text-[#f5f5f5] text-[36px] tracking-tight`}
        >
          Our Model
        </h1>
        <p
          className={`${dmSansRegular.className} mt-2 text-[#f5f5f5] text-[16px]`}
        >
          Trained on 60,000 diamonds from 2022
        </p>
      </div>
      <article className="mx-auto flex w-[75%] flex-col rounded-lg bg-white shadow-lg transition-all duration-200 hover:-translate-y-1 hover:shadow-xl">
        <h2
          className={`${dmSansRegular.className} px-6 pt-6 pb-3 text-center text-[28px] text-black`}
        >
          Model Performance
        </h2>
        <div className="relative mx-6 mb-6 aspect-[2/1] w-auto">
          <video
            src="/images/model-performance.mp4"
            className="absolute inset-0 h-full w-full object-contain"
            autoPlay
            loop
            muted
            playsInline
          />
        </div>
      </article>
    </section>
  );
}
