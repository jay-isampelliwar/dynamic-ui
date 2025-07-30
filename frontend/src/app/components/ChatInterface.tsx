"use client";

import { useDynamicUIChat } from "../hooks/useDynamicUIChat";
import DynamicUIChatHeader from "./DynamicUIChatHeader";
import DynamicUIChatInput from "./DynamicUIChatInput";
import DynamicUIMessageList from "./DynamicUIMessageList";

export default function DynamicUIChatInterface() {
  const { messages, isLoading, sendMessage, clearMessages } =
    useDynamicUIChat();

  return (
    <div className="flex flex-col h-screen bg-gray-50 w-1/2 mx-auto border-2 border-gray-200 rounded-lg">
      <DynamicUIChatHeader onClearMessages={clearMessages} />

      <div className="flex-1 overflow-y-auto px-6 py-4">
        <DynamicUIMessageList messages={messages} isLoading={isLoading} />
      </div>

      <div className="bg-white border-t border-gray-200 px-6 py-4">
        <DynamicUIChatInput onSendMessage={sendMessage} isLoading={isLoading} />
      </div>
    </div>
  );
}
