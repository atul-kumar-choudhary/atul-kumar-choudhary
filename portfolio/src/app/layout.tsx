import type { Metadata } from "next";
import { Geist_Mono } from "next/font/google";
import "./globals.css";

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Atul Kumar Choudhary - Portfolio",
  description: "Full Stack AI Engineer Portfolio",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`dark ${geistMono.variable} antialiased`}>
      <body className="bg-bg-base text-text-main font-mono h-screen terminal-scroll overflow-hidden flex flex-col">
        {children}
      </body>
    </html>
  );
}
