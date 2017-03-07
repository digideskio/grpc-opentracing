import abc

import six


class UnaryClientInterceptor(six.with_metaclass(abc.ABCMeta)):
  """Invokes custom code when a client-side, unary-unary RPC method is
      called.
    """

  @abc.abstractmethod
  def intercept_unary(self, method, request, metadata, invoker):
    """A function to be called when a client-side, unary-unary RPC method is
          invoked.

        Args:
          method: A string of the fully qualified method name being called.
          request: The request value for the RPC.
          metadata: Optional :term:`metadata` to be transmitted to the
            service-side of the RPC.
          invoker:  The handler to complete the RPC on the client. It is the
            interceptor's responsibility to call it.

        Returns:
          The result from calling invoker(request, metadata).
        """
    raise NotImplementedError()


class StreamClientInfo(six.with_metaclass(abc.ABCMeta)):
  """Consists of various information about a stream RPC on the client-side.

    Attributes:
      full_method: A string of the full RPC method, i.e.,
        /package.service/method.
      is_client_stream: Indicates whether the RPC is client-streaming.
      is_server_stream: Indicates whether the RPC is server-streaming.
    """


class StreamClientInterceptor(six.with_metaclass(abc.ABCMeta)):
  """Invokes custom code when a client-side, unary-stream, stream-unary, or
      stream-stream RPC method is called.
    """

  @abc.abstractmethod
  def intercept_stream(self, metadata, client_info, invoker):
    """A function to be called when a client-side, unary-stream,
          stream-unary, or stream-stream RPC method is invoked.

        Args:
          metadata: Optional :term:`metadata` to be transmitted to the
            service-side of the RPC.
          client_info: A StreamClientInfo containing various information about
            the RPC.
          invoker:  The handler to complete the RPC on the client. It is the
            interceptor's responsibility to call it.

        Returns:
          The result from calling invoker(metadata).
        """
    raise NotImplementedError()


# TODO: support multiple interceptor arguments
def intercept_channel(channel, interceptor):
  from grpcext import _interceptor
  return _interceptor.intercept_channel(channel, interceptor)


class UnaryServerInfo(six.with_metaclass(abc.ABCMeta)):
  """Consists of various information about a unary RPC on the server-side.

    Attributes:
      full_method: A string of the full RPC method, i.e.,
        /package.service/method.
    """


class StreamServerInfo(six.with_metaclass(abc.ABCMeta)):
  """Consists of various information about a stream RPC on the server-side.

    Attributes:
      full_method: A string of the full RPC method, i.e.,
        /package.service/method.
      is_client_stream: Indicates whether the RPC is client-streaming.
      is_server_stream: Indicates whether the RPC is server-streaming.
    """


class UnaryServerInterceptor(six.with_metaclass(abc.ABCMeta)):
  """Invokes custom code when a server-side, unary-unary RPC method is
      called.
    """

  @abc.abstractmethod
  def intercept_unary(self, request, metadata, server_info, handler):
    """A function to be called when a server-side, unary-unary RPC method is
          invoked.

        Args:
          request: The request value for the RPC.
          metadata: Optional :term:`metadata` transmitted from the client-side
            of the RPC.
          server_info: A UnaryServerInfo containing various information about
            the RPC.
          handler:  The handler to complete the RPC on the server. It is the
            interceptor's responsibility to call it.

        Returns:
          The result from calling handler(request).
        """
    raise NotImplementedError()


class StreamServerInterceptor(six.with_metaclass(abc.ABCMeta)):
  """Invokes custom code when a server-side, unary-stream, stream-unary, or
      stream-stream, RPC method is called.
    """

  @abc.abstractmethod
  def intercept_stream(self, metadata, server_info, handler):
    """A function to be called when a server-side, unary-stream,
          stream-unary, or stream-stream RPC method is invoked.

        Args:
          metadata: Optional :term:`metadata` transmitted from the client-side
            of the RPC.
          server_info: A StreamServerInfo containing various information about
            the RPC.
          handler:  The handler to complete the RPC on the server. It is the
            interceptor's responsibility to call it.

        Returns:
          The result from calling handler().
        """
    raise NotImplementedError()


# TODO: support multiple interceptor arguments
def intercept_server(server, interceptor):
  from grpcext import _interceptor
  return _interceptor.intercept_server(server, interceptor)


###################################  __all__  #################################


__all__ = (
    'UnaryClientInterceptor',
    'StreamClientInfo',
    'StreamClientInterceptor',
    'UnaryServerInfo',
    'StreamServerInfo',
    'UnaryServerInterceptor',
    'StreamServerInterceptor',
    'intercept_channel',
    'intercept_server',
)
