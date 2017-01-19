
.. image:: http://genomicsandhealth.org/files/logo_ga.png

=============
GA4GH Schemas
=============

This is the GA4GH schemas compiled as Protocol Buffers descriptors. It can be used 
describe and serialize genomics data using a standard interchange format.

.. code-block:: python

    import ga4gh.schemas.ga4gh.variants_pb2 as variants
    my_variant = variants.Variant(
        reference_name="1",
        start=1832,
        end=4123,
        reference_bases="A",
        alternate_bases=["C"])

Full documentation is available at `read-the-docs.org
<http://ga4gh-schemas.readthedocs.io/en/stable/>`_.

- To read more about how the GA4GH API uses Protocol Buffers, see `here <http://ga4gh-schemas.readthedocs.io/en/stable/appendix/proto_intro.html>`_.
