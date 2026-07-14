import type { Metadata } from "next";
import localFont from "next/font/local";
import { Geist, Geist_Mono } from "next/font/google";
import Image from "next/image";
import Link from "next/link";
import gemIqLogo from "../images/gemiq-logo.png";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

const iosevkaBold = localFont({
  src: "../fonts/Iosevka/IosevkaNerdFont-Bold.ttf",
  variable: "--font-iosevka-bold",
  display: "swap",
});

export const metadata: Metadata = {
  title: "GemIQ-ML",
  description: "Diamond price prediction model web application",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} ${iosevkaBold.variable} h-full antialiased`}
    >
      <body className="h-full flex flex-col">
        <header className="h-14 shrink-0 bg-[#2051eb] flex items-center justify-between px-6">
          <div className="flex items-center gap-2">
            <Image
              src={gemIqLogo}
              alt="GemIQ logo"
              width={36}
              height={36}
              className="h-12 w-12 object-contain"
              priority
            />
            <span
              className={`${iosevkaBold.className} text-[#f5f5f5] text-[30px] tracking-tight`}
            >
              GemIQ
            </span>
          </div>
          <nav className={`${iosevkaBold.className} flex items-center gap-6 text-[#f5f5f5] text-[24px]`}>
            <Link href="/" className="inline-block transition-transform duration-200 hover:-translate-y-1">
              Home
            </Link>
            <Link href="/predict" className="inline-block transition-transform duration-200 hover:-translate-y-1">
              Predict
            </Link>
          </nav>
        </header>
        <main className="flex-1 overflow-y-auto bg-[#2051eb]">{children}</main>
      </body>
    </html>
  );
}
