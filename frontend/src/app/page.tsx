import ChatInterface from "@/app/components/ChatInterface";
import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col h-screen w-full bg-gray-50">
      <ChatInterface />
    </div>
  );
}
