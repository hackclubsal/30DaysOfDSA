<script>


	function sortBinaryArray(a, n)
	{
		let j = -1;
		for (let i = 0; i < n; i++) {

			if (a[i] < 1) {
				j++;
				let temp = a[j];
				a[j] = a[i];
				a[i] = temp;
			}
		}
	}

		let a = [ 1, 0, 1, 0, 1, 0, 0, 1 ];

		let n = a.length;

		sortBinaryArray(a, n);

		for (let i = 0; i < n; i++)
			document.write(a[i] + " ");
</script>
