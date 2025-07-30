"use client";

import { useUITestChat } from "../hooks/useUITestChat";
import UITestChatHeader from "./UITestChatHeader";
import UITestChatInput from "./UITestChatInput";
import UITestMessageList from "./UITestMessageList";

export default function UITestChatInterface() {
  const { messages, isLoading, sendMessage, clearMessages } = useUITestChat();

  return (
    <div className="flex flex-col h-screen bg-gray-50 w-1/2 mx-auto border-2 border-gray-200 rounded-lg">
      <UITestChatHeader onClearMessages={clearMessages} />

      <div className="flex-1 overflow-y-auto px-6 py-4">
        <UITestMessageList messages={messages} isLoading={isLoading} />
      </div>

      <div className="bg-white border-t border-gray-200 px-6 py-4">
        <UITestChatInput onSendMessage={sendMessage} isLoading={isLoading} />
      </div>
    </div>
  );
}
