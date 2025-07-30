"use client";

import { DynamicUIMessage } from "../lib";
import DynamicUIFormComponent from "./DynamicUIFormComponent";

interface DynamicUIMessageListProps {
  messages: DynamicUIMessage[];
  isLoading: boolean;
}

export default function DynamicUIMessageList({
  messages,
  isLoading,
}: DynamicUIMessageListProps) {
  if (messages.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center h-full text-center text-gray-500">
        <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mb-4">
          <svg
            className="w-8 h-8 text-blue-500"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
            />
          </svg>
        </div>
        <h3 className="text-lg font-medium mb-2">Dynamic UI Generator</h3>
        <p className="text-sm max-w-md">
          Ask me to create any form fields you need. For example:
        </p>
        <div className="mt-4 space-y-2 text-left">
          <p className="text-xs bg-gray-100 p-2 rounded">
            • "I need name, email and date picker"
          </p>
          <p className="text-xs bg-gray-100 p-2 rounded">
            • "Create a form with address fields"
          </p>
          <p className="text-xs bg-gray-100 p-2 rounded">
            • "Generate a dropdown with options"
          </p>
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {messages.map((message) => (
        <div
          key={message.id}
          className={`flex ${
            message.role === "user" ? "justify-end" : "justify-start"
          }`}
        >
          <div
            className={`max-w-[80%] ${
              message.role === "user"
                ? "bg-blue-500 text-white rounded-lg rounded-br-none"
                : "bg-white border text-black border-gray-200 rounded-lg rounded-bl-none"
            } px-4 py-3`}
          >
            <div className="whitespace-pre-wrap">{message.content}</div>
            {message.component && typeof message.component === "object" && (
              <div className="mt-4">
                <DynamicUIFormComponent component={message.component} />
              </div>
            )}
            <div
              className={`text-xs mt-2 ${
                message.role === "user" ? "text-blue-100" : "text-gray-500"
              }`}
            >
              {message.timestamp.toLocaleTimeString()}
            </div>
          </div>
        </div>
      ))}

      {isLoading && (
        <div className="flex justify-start">
          <div className="bg-white border border-gray-200 rounded-lg rounded-bl-none px-4 py-3">
            <div className="flex items-center space-x-2">
              <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
              <div
                className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                style={{ animationDelay: "0.1s" }}
              ></div>
              <div
                className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"
                style={{ animationDelay: "0.2s" }}
              ></div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
