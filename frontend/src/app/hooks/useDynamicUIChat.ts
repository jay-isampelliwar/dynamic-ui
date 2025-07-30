import { useState, useCallback } from 'react'
import { DynamicUIMessage } from '../lib'
import { dynamicUIApiService } from '@/app/lib/dynamicUIApi'

export function useDynamicUIChat() {
  const [messages, setMessages] = useState<DynamicUIMessage[]>([])
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const sendMessage = useCallback(async (content: string) => {
    if (!content.trim() || isLoading) return

    const userMessage: DynamicUIMessage = {
      id: Date.now().toString(),
      content: content.trim(),
      role: 'user',
      timestamp: new Date()
    }

    setMessages(prev => [...prev, userMessage])
    setIsLoading(true)
    setError(null)

    try {
      const response = await dynamicUIApiService.sendDynamicUIMessage(content.trim())
      
      // Parse the response to extract component if present
      let messageContent = response.content;
      let component = response.component;

      console.log("response", response)

      // Ensure component is properly typed
      if (component && typeof component === 'object' && 'type' in component && 'fields' in component) {
        // Component is valid, use it as is
        console.log('Valid component received:', component);
      } else if (component) {
        // Component exists but might not be properly formatted
        console.warn('Component received but format is unexpected:', component);
        component = null;
      } else {
        console.log('No component received in response');
      }
      
      const assistantMessage: DynamicUIMessage = {
        id: (Date.now() + 1).toString(),
        content: messageContent,
        role: 'assistant',
        timestamp: new Date(),
        component: component
      }

      setMessages(prev => [...prev, assistantMessage])
    } catch (err) {
      console.error('Error sending message:', err)
      const errorMessage = err instanceof Error ? err.message : 'An unexpected error occurred'
      setError(errorMessage)
      
      const errorResponse: DynamicUIMessage = {
        id: (Date.now() + 1).toString(),
        content: 'Sorry, I encountered an error. Please try again. ' + errorMessage,
        role: 'assistant',
        timestamp: new Date()
      }
      setMessages(prev => [...prev, errorResponse])
    } finally {
      setIsLoading(false)
    }
  }, [isLoading])

  const clearMessages = useCallback(() => {
    setMessages([])
    setError(null)
  }, [])

  const clearError = useCallback(() => {
    setError(null)
  }, [])

  return {
    messages,
    isLoading,
    error,
    sendMessage,
    clearMessages,
    clearError
  }
} 