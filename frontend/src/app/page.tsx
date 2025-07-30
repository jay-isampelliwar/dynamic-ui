import ChatInterface from "@/app/components/ChatInterface";
import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col h-screen w-full bg-gray-50">
      {/* Navigation Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center">
              <h1 className="text-xl font-semibold text-gray-900">
                AI Assistant
              </h1>
            </div>
            <nav className="flex space-x-8">
              <Link
                href="/"
                className="text-gray-900 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium transition-colors"
              >
                Chat
              </Link>
              <Link
                href="/forms"
                className="text-gray-500 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium transition-colors"
              >
                Dynamic Forms
              </Link>
              <Link
                href="/agent"
                className="text-gray-500 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium transition-colors"
              >
                Agent Chat
              </Link>
              <Link
                href="/ui"
                className="text-gray-500 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium transition-colors"
              >
                Resume Builder
              </Link>
              <Link
                href="/ui-test"
                className="text-gray-500 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium transition-colors"
              >
                UI Test
              </Link>
            </nav>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <div className="flex-1">
        <ChatInterface />
      </div>
    </div>
  );
}
