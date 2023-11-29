def example():
    st.write(
        """
        This is an example of a date range picker that *always* returns a start and
        end date, even if the user has only selected one of the dates. Until the
        user selects both dates, the app will not run.
        """
    )
    result = date_range_picker("Select a date range")
    st.write("Result:", result)
